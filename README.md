**Why do we name the tests test_1, test_2, etc.?**

In Python's `unittest` framework, the function names that begin with `test_` are automatically detected and executed by the test runner. Prefixing them with `test_1`, `test_2`, etc., helps ensure they run in a specific order, especially useful when one test depends on another (e.g., posting before getting). Although in principle each test should be independent, controlled ordering can help during development and debugging.

---

**What is the function of the payload variable?**

The `payload` variable typically stores data that is being sent in the body of an HTTP request, especially in `POST` requests. In the context of testing an API, this dictionary contains the structured input (like a task or student object) to be serialized to JSON and posted to the API endpoint. It mimics how a frontend or client would interact with the backend.

---

**What is the function of the assertEqual function?**

The `assertEqual(a, b)` function checks whether two values are equal, and if not, it causes the test to fail. In API testing, it is used to verify that the response data or status code matches expected output. For example, if a `GET` request is supposed to return a JSON object, `assertEqual` confirms that the returned data structure matches the test expectation exactly.

---
