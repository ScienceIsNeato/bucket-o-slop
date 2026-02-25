/**
 * Tests for string utility functions.
 *
 * MAIN BRANCH: Every test has at least one assertion.
 */

describe("String Utils", () => {
  test("trims whitespace", () => {
    const result = "  hello  ".trim();
    expect(result).toBe("hello");
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
