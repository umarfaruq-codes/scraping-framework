import logging
import time

import requests

logger = logging.getLogger(__name__)

class HTTPClient:

    def __init__(self, headers = None):
        self.session = requests.Session()

        if headers:
            self.session.headers.update(headers)

    def fetch(
        self,
        url : str, 
        params : dict | None=None, 
        timeout : tuple[float, float] = (5,20),
        max_retries : int = 3
    ) -> requests.Response:

        if max_retries<1:
            raise ValueError("Attempts must be atleast 1")

        retryable_statuses = {429, 500, 502, 503, 504}

        for attempt in range(1, (max_retries+1)):
            try:
                logger.info("Requesting %s. Attempt (%d/%d)",
                            url,
                            attempt,
                            max_retries)
                
                response = self.session.get(url, params=params, timeout=timeout)

                if response.status_code in retryable_statuses:
                    
                    if attempt == max_retries:
                        response.raise_for_status() 

                    retry_after = response.headers.get("Retry-After") 

                    try:
                        delay = float(retry_after) if retry_after else 2**(attempt)  
                    except ValueError:
                        delay = 2**(attempt)  

                    delay = min(max(delay, 0), 60)

                    logger.warning("Retryable HTTP %d from %s. "
                                "Attempt %d/%d; Waiting %.1fs",
                                response.status_code,
                                url,
                                attempt,
                                max_retries,
                                delay)

                    time.sleep(delay) 
                    continue 

                
                response.raise_for_status()

                logger.info("Request secceeded: %s (HTTP %d)",
                            url,
                            response.status_code)

                return response 

            except (requests.Timeout, requests.ConnectionError) as exc:
                if attempt == max_retries: 
                    logger.error("Request failed after %d attempts: %s (%s)",
                                attempt,
                                url,
                                type(exc).__name__)
                    raise
                
                delay = 2**attempt

                logger.warning("%s for %s. Attempt %d/%d; retrying in %d seconds.",
                                type(exc).__name__,
                                url,
                                attempt,
                                max_retries,
                                delay,)

                time.sleep(delay)

        raise RuntimeError("Request loop ended unexpectedly")