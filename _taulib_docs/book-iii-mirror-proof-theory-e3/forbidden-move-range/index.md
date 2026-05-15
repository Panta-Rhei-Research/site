---
{
  "projection_kind": "taulib_declaration",
  "title": "forbidden_move_range",
  "permalink": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/forbidden-move-range/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Mirror.ProofTheoryE3`.",
  "declaration_id": "TauLib.BookIII.Mirror.ProofTheoryE3::forbidden_move_range",
  "declaration_slug": "forbidden-move-range",
  "kind": "theorem",
  "name": "forbidden_move_range",
  "module_name": "TauLib.BookIII.Mirror.ProofTheoryE3",
  "module_url": "/corpus/taulib/docs/book-iii-mirror-proof-theory-e3/",
  "source_line_start": 363,
  "source_line_end": 364,
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
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L363-L364",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L363-L364",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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
- Source path: [`TauLib/BookIII/Mirror/ProofTheoryE3.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/ProofTheoryE3.lean#L363-L364)
- Source range: L363-L364
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D75` — E₂→E₃ Boundary Crossing

## Immediate Comment / Docstring

```lean
/-- [III.D75] Structural: forbidden move indices cover 0..3. -/
```

## Source Excerpt

```lean
theorem forbidden_move_range :
    all_paradoxes.map Paradox.forbidden_move_idx = [0, 1, 2, 3] := rfl
```
