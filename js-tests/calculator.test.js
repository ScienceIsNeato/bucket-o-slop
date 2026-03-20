/**
 * Tests for a hypothetical calculator module.
 *
 * ALL-FAIL BRANCH: Classic LLM slop — tests that compute results
 * but never verify them with expect(). Every test here is a false
 * positive: it passes regardless of whether the code works.
 *
 * The js-expect-assert gate should FAIL on this branch.
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
    const product = 3 * 7;
    expect(product).toBe(21);
  });

  test("divides two numbers", () => {
    const result = 20 / 5;
    expect(result).toBe(4);
  });

  test("handles division by zero", () => {
    const result = 1 / 0;
    expect(result).toBe(Infinity);
  });
});
