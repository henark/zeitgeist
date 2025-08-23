# 360Giving Website: Analysis and Skill Development Plan

This document outlines the execution plan for analyzing the `https://www.360giving.org` website. This task is part of a specific directive to "learn and develop skill" with the `view_text_website` tool, focusing on intelligent parsing and information architecture.

## Phase 1: Initial Access and Structural Parsing

The first step is to access the homepage and parse its content in a structured manner. The goal is to move beyond simple text fetching to a more intelligent extraction of the page's components.

### Expected Structured Output

The raw text from the homepage will be parsed and populated into the following JSON structure. This serves as a template to guide the information extraction process.

```json
{
  "pageTitle": "...",
  "mainHeading": "...",
  "tagline": "...",
  "navigationLinks": {
    "About Us": "/about",
    "Our Work": "/work",
    "Data Standard": "/standard",
    "Get Involved": "/involved"
  },
  "keySections": [
    {
      "heading": "What is 360Giving?",
      "summary": "..."
    },
    {
      "heading": "The 360Giving Standard",
      "summary": "..."
    }
  ],
  "callToAction": {
    "text": "...",
    "link": "..."
  }
}
```

This structured approach is the core of the skill being developed. The next step is to use the `view_text_website` tool to fetch the data and populate this template.
