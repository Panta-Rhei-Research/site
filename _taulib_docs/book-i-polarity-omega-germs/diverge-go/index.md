---
{
  "projection_kind": "taulib_declaration",
  "title": "diverge_go",
  "permalink": "/verify/taulib/docs/book-i-polarity-omega-germs/diverge-go/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.OmegaGerms`.",
  "declaration_id": "TauLib.BookI.Polarity.OmegaGerms::diverge_go",
  "declaration_slug": "diverge-go",
  "kind": "def",
  "name": "diverge_go",
  "module_name": "TauLib.BookI.Polarity.OmegaGerms",
  "module_url": "/verify/taulib/docs/book-i-polarity-omega-germs/",
  "source_line_start": 195,
  "source_line_end": 203,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L195-L203",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.OmegaGerms",
        "url": "/verify/taulib/docs/book-i-polarity-omega-germs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L195-L203",
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

- Module: [TauLib.BookI.Polarity.OmegaGerms](/verify/taulib/docs/book-i-polarity-omega-germs/)
- Source path: [`TauLib/BookI/Polarity/OmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L195-L203)
- Source range: L195-L203
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Find first disagreement index between two component lists. -/
```

## Source Excerpt

```lean
def diverge_go (c1 c2 : List TauIdx) (d i : Nat) (fuel : Nat) : TauIdx :=
  if fuel = 0 then 0
  else if i ≥ d then 0
  else
    let a := c1.getD i 0
    let b := c2.getD i 0
    if a != b then i + 1
    else diverge_go c1 c2 d (i + 1) (fuel - 1)
termination_by fuel
```
