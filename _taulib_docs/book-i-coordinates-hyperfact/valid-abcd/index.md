---
{
  "projection_kind": "taulib_declaration",
  "title": "ValidABCD",
  "permalink": "/verify/taulib/docs/book-i-coordinates-hyperfact/valid-abcd/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.Hyperfact`.",
  "declaration_id": "TauLib.BookI.Coordinates.Hyperfact::ValidABCD",
  "declaration_slug": "valid-abcd",
  "kind": "def",
  "name": "ValidABCD",
  "module_name": "TauLib.BookI.Coordinates.Hyperfact",
  "module_url": "/verify/taulib/docs/book-i-coordinates-hyperfact/",
  "source_line_start": 42,
  "source_line_end": 45,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Hyperfact.lean#L42-L45",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.Hyperfact",
        "url": "/verify/taulib/docs/book-i-coordinates-hyperfact/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Hyperfact.lean#L42-L45",
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

- Module: [TauLib.BookI.Coordinates.Hyperfact](/verify/taulib/docs/book-i-coordinates-hyperfact/)
- Source path: [`TauLib/BookI/Coordinates/Hyperfact.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/Hyperfact.lean#L42-L45)
- Source range: L42-L45
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Predicate: (A,B,C,D) is a valid ABCD decomposition of X. -/
```

## Source Excerpt

```lean
def ValidABCD (x a b c d : TauIdx) : Prop :=
  a ≥ 2 ∧ b ≥ 1 ∧ c ≥ 1 ∧
  tower_atom a b c * d = x ∧
  (d = 0 ∨ ¬(a ∣ d))  -- D is A-free (or zero)
```
