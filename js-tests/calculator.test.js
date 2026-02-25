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
    console.log("result:", result);
    // No assertion — this always passes
  });

  test("subtracts two numbers", () => {
    const result = 10 - 4;
    // Computed but never checked
  });

  test("multiplies two numbers", () => {
    const product = 3 * 7;
    // Classic vibe-coded test: looks busy, proves nothing
    if (product > 0) {
      console.log("positive result");
    }
  });

  test("divides two numbers", () => {
    const result = 20 / 5;
    // This test passes even if division is broken
  });

  test("handles division by zero", () => {
    const result = 1 / 0;
    // Should assert Infinity — but doesn't
    console.log("divided:", result);
  });
});
