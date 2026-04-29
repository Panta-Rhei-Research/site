---
{
  "projection_kind": "taulib_declaration",
  "title": "verify_descent_up_to_go",
  "permalink": "/verify/taulib/docs/book-i-coordinates-descent/verify-descent-up-to-go/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.Descent`.",
  "declaration_id": "TauLib.BookI.Coordinates.Descent::verify_descent_up_to_go",
  "declaration_slug": "verify-descent-up-to-go",
  "kind": "def",
  "name": "verify_descent_up_to_go",
  "module_name": "TauLib.BookI.Coordinates.Descent",
  "module_url": "/verify/taulib/docs/book-i-coordinates-descent/",
  "source_line_start": 73,
  "source_line_end": 77,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Descent.lean#L73-L77",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.Descent",
        "url": "/verify/taulib/docs/book-i-coordinates-descent/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Descent.lean#L73-L77",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookI.Coordinates.Descent](/verify/taulib/docs/book-i-coordinates-descent/)
- Source path: [`TauLib/BookI/Coordinates/Descent.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Descent.lean#L73-L77)
- Source range: L73-L77
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Verify descent for all X from 2 to n. -/
```

## Source Excerpt

```lean
def verify_descent_up_to_go (i n : Nat) (fuel : Nat) : Bool :=
  if fuel = 0 then true
  else if i > n then true
  else full_descent_check i && verify_descent_up_to_go (i + 1) n (fuel - 1)
termination_by fuel
```
