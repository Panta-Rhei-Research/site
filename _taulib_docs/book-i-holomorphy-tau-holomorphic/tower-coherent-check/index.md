---
{
  "projection_kind": "taulib_declaration",
  "title": "tower_coherent_check",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/tower-coherent-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Holomorphy.TauHolomorphic`.",
  "declaration_id": "TauLib.BookI.Holomorphy.TauHolomorphic::tower_coherent_check",
  "declaration_slug": "tower-coherent-check",
  "kind": "def",
  "name": "tower_coherent_check",
  "module_name": "TauLib.BookI.Holomorphy.TauHolomorphic",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/",
  "source_line_start": 76,
  "source_line_end": 80,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L76-L80",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.TauHolomorphic",
        "url": "/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L76-L80",
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

- Module: [TauLib.BookI.Holomorphy.TauHolomorphic](/verify/taulib/docs/book-i-holomorphy-tau-holomorphic/)
- Source path: [`TauLib/BookI/Holomorphy/TauHolomorphic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/TauHolomorphic.lean#L76-L80)
- Source range: L76-L80
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Decidable tower coherence check at given stages (for concrete values). -/
```

## Source Excerpt

```lean
def tower_coherent_check (f : StageFun) (n k l : TauIdx) : Bool :=
  if k > l then true
  else
    (reduce (f.b_fun n l) k == f.b_fun n k) &&
    (reduce (f.c_fun n l) k == f.c_fun n k)
```
