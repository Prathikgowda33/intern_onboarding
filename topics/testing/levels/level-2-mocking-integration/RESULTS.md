# Results — Level 2 (Mocking & Integration)

| Constraint | Result | Evidence (command + what you observed) |
|------------|--------|--------------------------------------|
| C1: All tests pass | PASS | pytest test_weather_reporter.py -v → 8 passed |
| C2: At least 7 tests | PASS | pytest test_weather_reporter.py --collect-only → 8 tests collected |
| C3: unittest.mock.patch used | PASS | grep -n "patch" test_weather_reporter.py → multiple @patch decorators on weather_reporter.requests.get |
| C4: Error handling tested | PASS | grep showed 404 status test, ValueError test, and Timeout side_effect test |
| C5: side_effect for multiple returns | PASS | mock_get.side_effect = [ok, bad] and Timeout side_effect used |
| C6: Integration test exists | PASS | test_integration_pipeline calls get_current_weather() and format_weather_report() together |
| C7: No real HTTP calls | PASS | All requests.get calls mocked with @patch("weather_reporter.requests.get") |

## Overall

- [x] CLEARED — all constraints pass. Testing topic complete.
- [ ] Not cleared

## Notes

Learned unittest.mock.patch, MagicMock, side_effect, mocking external APIs, and integration testing.
