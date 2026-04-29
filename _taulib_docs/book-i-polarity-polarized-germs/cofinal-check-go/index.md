---
{
  "projection_kind": "taulib_declaration",
  "title": "cofinal_check_go",
  "permalink": "/verify/taulib/docs/book-i-polarity-polarized-germs/cofinal-check-go/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.PolarizedGerms`.",
  "declaration_id": "TauLib.BookI.Polarity.PolarizedGerms::cofinal_check_go",
  "declaration_slug": "cofinal-check-go",
  "kind": "def",
  "name": "cofinal_check_go",
  "module_name": "TauLib.BookI.Polarity.PolarizedGerms",
  "module_url": "/verify/taulib/docs/book-i-polarity-polarized-germs/",
  "source_line_start": 79,
  "source_line_end": 84,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PolarizedGerms.lean#L79-L84",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.PolarizedGerms",
        "url": "/verify/taulib/docs/book-i-polarity-polarized-germs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PolarizedGerms.lean#L79-L84",
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

- Module: [TauLib.BookI.Polarity.PolarizedGerms](/verify/taulib/docs/book-i-polarity-polarized-germs/)
- Source path: [`TauLib/BookI/Polarity/PolarizedGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PolarizedGerms.lean#L79-L84)
- Source range: L79-L84
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Computable check: does the sequence have a nonzero value between from_depth and to_depth? -/
```

## Source Excerpt

```lean
def cofinal_check_go (f : Nat → Nat) (i to_depth : Nat) (fuel : Nat) : Bool :=
  if fuel = 0 then false
  else if i > to_depth then false
  else if f i ≠ 0 then true
  else cofinal_check_go f (i + 1) to_depth (fuel - 1)
termination_by fuel
```
