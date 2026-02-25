/**
 * Tests for a hypothetical calculator module.
 *
 * MIXED BRANCH: All JS tests have proper assertions.
 * The js-expect-assert gate should PASS on this branch,
 * while Python-specific gates (security, dead-code, bogus-tests)
 * intentionally fail — demonstrating a "mixed" outcome.
 */

describe("Calculator", () => {
  test("adds two positive numbers", () => {
    const result = 2 + 3;
    expect(result).toBe(5);
  });

  test("subtracts two numbers", () => {
    const result = 10 - 4;
    expect(result).toBe(6);
  });

  test("multiplies two numbers", () => {
    expect(3 * 7).toBe(21);
  });

  test("divides two numbers", () => {
    const result = 20 / 5;
    expect(result).toBe(4);
  });

  test("handles division by zero", () => {
    expect(1 / 0).toBe(Infinity);
  });
});
