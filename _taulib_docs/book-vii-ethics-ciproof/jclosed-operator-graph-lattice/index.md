---
{
  "projection_kind": "taulib_declaration",
  "title": "JClosedOperatorGraphLattice",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/jclosed-operator-graph-lattice/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::JClosedOperatorGraphLattice",
  "declaration_slug": "jclosed-operator-graph-lattice",
  "kind": "structure",
  "name": "JClosedOperatorGraphLattice",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 473,
  "source_line_end": 482,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L473-L482",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/verify/taulib/docs/book-vii-ethics-ciproof/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L473-L482",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L473-L482)
- Source range: L473-L482
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The lattice of j_dig-closed operator graphs F.
    Key property: F is a complete lattice (arbitrary intersections
    of j-closed operator graphs preserve j-closure). -/
```

## Source Excerpt

```lean
structure JClosedOperatorGraphLattice where
  /-- Non-empty (Kernel Theorem VII.T36 guarantees). -/
  non_empty : Bool := true
  /-- Closed under arbitrary intersection. -/
  intersection_closed : Bool := true
  /-- Forms complete lattice. -/
  complete_lattice : Bool := true
  /-- Has unique minimum element. -/
  has_unique_minimum : Bool := true
  deriving Repr
```
