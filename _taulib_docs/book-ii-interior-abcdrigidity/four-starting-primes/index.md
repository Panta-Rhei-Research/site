---
{
  "projection_kind": "taulib_declaration",
  "title": "four_starting_primes",
  "permalink": "/corpus/taulib/docs/book-ii-interior-abcdrigidity/four-starting-primes/",
  "summary_short": "`def` declaration in `TauLib.BookII.Interior.ABCDRigidity`.",
  "declaration_id": "TauLib.BookII.Interior.ABCDRigidity::four_starting_primes",
  "declaration_slug": "four-starting-primes",
  "kind": "def",
  "name": "four_starting_primes",
  "module_name": "TauLib.BookII.Interior.ABCDRigidity",
  "module_url": "/corpus/taulib/docs/book-ii-interior-abcdrigidity/",
  "source_line_start": 93,
  "source_line_end": 93,
  "registry_ids": [
    "II.R04"
  ],
  "related_registry_items": [
    {
      "id": "II.R04",
      "title": "ABCD vs Quaternions",
      "url": "/registry/object/II.R04/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/ABCDRigidity.lean#L93-L93",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Interior.ABCDRigidity",
        "url": "/corpus/taulib/docs/book-ii-interior-abcdrigidity/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/ABCDRigidity.lean#L93-L93",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookII.Interior.ABCDRigidity](/corpus/taulib/docs/book-ii-interior-abcdrigidity/)
- Source path: [`TauLib/BookII/Interior/ABCDRigidity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Interior/ABCDRigidity.lean#L93-L93)
- Source range: L93-L93
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- `II.R04` — ABCD vs Quaternions

## Immediate Comment / Docstring

```lean
/-- [II.R04] Key structural difference: ABCD uses one-sided rays (ℕ),
    not two-sided axes (ℝ). Rays have a starting prime but no origin.

    The four starting primes are distinct:
    α₁ = 2, π₁ = 3, γ₁ = 5, η₁ = 7. -/
```

## Source Excerpt

```lean
def four_starting_primes : List TauIdx := [2, 3, 5, 7]
```
