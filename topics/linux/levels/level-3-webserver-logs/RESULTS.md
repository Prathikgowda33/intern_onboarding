# Results — Linux (Webserver Logs)

## Constraint results

| Constraint | Result | Evidence |
|------------|--------|----------|
| C1 | PASS | docker run -d --name nginx-logs -p 8080:80 nginx -> container 83efca5bb40c... |
| C2 | PASS | head -3 captured-access.log showed nginx access logs starting with IPs; wc -l = 60 |
| C3 | PASS | awk '$9 ~ /^4[0-9][0-9]$/' captured-access.log \| wc -l -> 10 |
| C4 | PASS | ./analyze-live.sh captured-access.log printed all 4 sections |
| C5 | PASS | ./analyze-live.sh with no arguments printed Usage: ./analyze-live.sh <logfile> [N] |
| C6 | PASS | Script reported 4xx=10, 5xx=0; independent counts matched |
| C7 | PASS | Total requests processed: 60 matched wc -l |
| C8 | PASS | docker ps -a \| grep nginx-logs returned no output after cleanup |

## Overall

✅ CLEARED — all constraints pass. Topic complete.
