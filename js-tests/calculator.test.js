/**
 * Tests for a hypothetical calculator module.
 *
 * MAIN BRANCH: All tests contain proper expect() assertions.
 * The js-expect-assert gate should PASS on this branch.
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

  test("converts to uppercase", () => {
    expect("hello".toUpperCase()).toBe("HELLO");
  });

  test("checks string contains substring", () => {
    const str = "the quick brown fox";
    expect(str).toContain("quick");
  });

  it("splits on delimiter", () => {
    const parts = "a,b,c".split(",");
    expect(parts).toHaveLength(3);
    expect(parts[0]).toBe("a");
  });
});
