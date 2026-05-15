---
{
  "projection_kind": "taulib_declaration",
  "title": "Paradox.forbidden_move_idx",
  "permalink": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/forbidden-move-idx/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.ProofTheoryE3`.",
  "declaration_id": "TauLib.BookIII.Mirror.ProofTheoryE3::Paradox.forbidden_move_idx",
  "declaration_slug": "forbidden-move-idx",
  "kind": "def",
  "name": "Paradox.forbidden_move_idx",
  "module_name": "TauLib.BookIII.Mirror.ProofTheoryE3",
  "module_url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/",
  "source_line_start": 89,
  "source_line_end": 93,
  "registry_ids": [
    "III.D75"
  ],
  "related_registry_items": [
    {
      "id": "III.D75",
      "title": "E₂→E₃ Boundary Crossing",
      "url": "/registry/object/III.D75/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L89-L93",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.ProofTheoryE3",
        "url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L89-L93",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookIII.Mirror.ProofTheoryE3](/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/)
- Source path: [`TauLib/BookIII/Mirror/ProofTheoryE3.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L89-L93)
- Source range: L89-L93
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- `III.D75` — E₂→E₃ Boundary Crossing

## Immediate Comment / Docstring

```lean
/-- [III.D75] Forbidden move type associated with each paradox.
    Maps each classical paradox to the structural violation it encodes.
    0 = unbounded_fanout, 1 = global_equality,
    2 = succinct_circuits, 3 = exponential_quantification -/
```

## Source Excerpt

```lean
def Paradox.forbidden_move_idx : Paradox -> Nat
  | .Cantor  => 0  -- unbounded_fanout
  | .Russell => 1  -- global_equality
  | .Goedel  => 2  -- succinct_circuits
  | .Turing  => 3  -- exponential_quantification
```
