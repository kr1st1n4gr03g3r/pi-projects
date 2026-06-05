# hardware_checks

Component go/no-go tests for the Pico 2 W. Each test confirms a piece of hardware is working before building a full project on top of it.

---

## Tests

| Test | What it checks |
|---|---|
| [lcd1602_power_check](./lcd1602_power_check.json) | Powers the 1602A LCD via the Pico 2 W. Confirms backlight turns on and contrast squares appear on the top row. No code required. |

---

## How to use

Each test has a Wokwi diagram (`.json`) and a reference screenshot (`.png`).

- **Simulate:** open the `.json` in [Wokwi](https://wokwi.com)
- **Physical:** follow the wiring in the diagram on your breadboard

---

## Notes

- These are not projects. They are pass/fail checks.
- A passing test means the component is alive and worth wiring up fully.
