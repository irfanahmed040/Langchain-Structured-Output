# LangChain Structured Output Examples

This repository demonstrates how to generate **structured outputs from Large Language Models (LLMs)** using **LangChain**.

Instead of receiving raw text responses from an LLM, structured output allows the model to return **validated, machine-readable data** such as dictionaries, Pydantic objects, or typed schemas.

The project demonstrates multiple schema approaches:

* JSON Schema
* Pydantic Models
* Python TypedDict

It also includes examples of **data validation using Pydantic and TypedDict**.

---

## Project Structure

```
LANGCHAIN-STRUCTURED-OUTPUT/
│
├── venv/
├── .env
│
├── json_schema.json
├── pydantic_demo.py
├── typeddict_demo.py
│
├── with_structuredoutput_json.py
├── with_structuredoutput_pydantic.py
├── with_structuredoutput_typeddict.py
```

---

## Files Explained

### json_schema.json

A simple **JSON schema** describing a student object.

Example schema:

```
{
  "title": "student",
  "description": "schema about students",
  "type": "object",
  "properties": {
    "name": "string",
    "age": "integer"
  },
  "required": ["name"]
}
```

This file demonstrates how structured data can be defined using **JSON Schema**.

---

## pydantic_demo.py

Demonstrates **data validation using Pydantic models**.

Features demonstrated:

* Default values
* Optional fields
* Email validation
* Numeric validation using constraints
* Converting Pydantic objects to dictionaries
* Exporting objects to JSON

Example model:

```
class Student(BaseModel):
    name: str = "irfan"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10)
```

Pydantic automatically validates:

* Email format
* CGPA range
* Data types

---

## typeddict_demo.py

Shows how **Python TypedDict** can define structured data types.

Example:

```
class Person(TypedDict):
    name: str
    age: int
```

TypedDict provides:

* Type checking
* Lightweight schema definition
* Static analysis support

---

## with_structuredoutput_json.py

Demonstrates **LangChain structured output using JSON Schema**.

Steps performed:

1. Define a schema using JSON format
2. Pass the schema to LangChain
3. Extract structured information from a product review

The LLM analyzes a **Samsung Galaxy S24 Ultra product review** and extracts:

* Key themes
* Summary
* Sentiment
* Pros
* Cons
* Reviewer name

Example:

```
structured_model = model.with_structured_output(json_schema)
result = structured_model.invoke(review_text)
```

Output is returned as a **Python dictionary**.

---

## with_structuredoutput_pydantic.py

Demonstrates structured output using **Pydantic models**.

Example schema:

```
class Review(BaseModel):
    key_themes: list[str]
    summary: str
    sentiment: str
    pros: Optional[list[str]]
    cons: Optional[list[str]]
    name: Optional[str]
```

LangChain automatically converts the model output into a **Pydantic object**.

Example usage:

```
print(result.pros)
print(result.name)
```

Benefits of Pydantic:

* Automatic validation
* Type safety
* Easy integration with Python applications

---

## with_structuredoutput_typeddict.py

Demonstrates structured output using **TypedDict with annotations**.

Example schema:

```
class Review(TypedDict):
    summary: Annotated[str, "Brief summary of the review"]
    sentiment: Annotated[str, "Sentiment of the review"]
    pros: Annotated[list[str], "List of pros"]
    cons: Annotated[list[str], "List of cons"]
    name: Annotated[Optional[str], "Reviewer name"]
```

Output is returned as a **dictionary**.

This approach is useful when you want:

* Lightweight schema definitions
* Native Python typing
* Minimal validation overhead

---

## Example Use Case

The repository processes a **Samsung Galaxy S24 Ultra review** and extracts structured information such as:

* Key themes discussed
* Overall sentiment
* Advantages and disadvantages
* Reviewer name

Instead of receiving raw text, the model returns **structured data that can be used programmatically**.

Example output:

```
{
  "key_themes": ["performance", "camera", "battery", "price"],
  "summary": "The Galaxy S24 Ultra offers powerful performance and an excellent camera but is expensive and bulky.",
  "sentiment": "positive",
  "pros": [
      "Powerful Snapdragon processor",
      "Excellent 200MP camera",
      "Long battery life",
      "S-Pen support"
  ],
  "cons": [
      "Heavy and bulky",
      "Bloatware in One UI",
      "Expensive"
  ],
  "name": "Irfan Mohammed"
}
```

---

## Requirements

Install dependencies:

```
pip install langchain langchain-openai python-dotenv pydantic
```

Optional:

```
pip install typing_extensions
```

---

## Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## Learning Goals

This project helps understand:

* Structured output generation from LLMs
* Schema validation techniques
* LangChain structured output APIs
* Differences between JSON Schema, Pydantic, and TypedDict
* Converting LLM responses into machine-readable data

---

## Model Compatibility with Structured Output

Not all LLM models support **native structured outputs**.

Some models do not support OpenAI's structured output API or JSON schema enforcement.

Examples of models that support structured output well:

* gpt-4o
* gpt-4o-mini
* gpt-4.1
* gpt-4.1-mini

Older models such as **gpt-3.5-turbo** may produce warnings and rely on fallback mechanisms like **function calling**.

When a model does not support structured outputs, developers often use **LangChain Output Parsers**.

Common parsers include:

* PydanticOutputParser
* StructuredOutputParser
* JsonOutputParser

These parsers convert raw LLM responses into structured data formats when the model cannot guarantee valid schema output.

---

## Key Takeaway

Structured output in LLM pipelines can be implemented in two ways:

1. **Native Structured Output**

   * Supported by newer models
   * More reliable schema-validated responses

2. **Output Parsers**

   * Used when models lack native structured output support
   * Parse raw text responses into structured formats

Understanding this distinction is important when building reliable AI pipelines.

---

## Technologies Used

* Python
* LangChain
* OpenAI API
* Pydantic
* JSON Schema
* TypedDict
* dotenv

---

## Author

Irfan Mohammed Ahmed
