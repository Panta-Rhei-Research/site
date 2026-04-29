---
{
  "projection_kind": "taulib_declaration",
  "title": "decompose_recovery",
  "permalink": "/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/decompose-recovery/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Regularity.IdempotentDecomposition`.",
  "declaration_id": "TauLib.BookII.Regularity.IdempotentDecomposition::decompose_recovery",
  "declaration_slug": "decompose-recovery",
  "kind": "theorem",
  "name": "decompose_recovery",
  "module_name": "TauLib.BookII.Regularity.IdempotentDecomposition",
  "module_url": "/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/",
  "source_line_start": 99,
  "source_line_end": 102,
  "registry_ids": [
    "II.L07"
  ],
  "related_registry_items": [
    {
      "id": "II.L07",
      "title": "Idempotent Decomposition Lemma",
      "url": "/registry/object/II.L07/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L99-L102",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.IdempotentDecomposition",
        "url": "/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L99-L102",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookII.Regularity.IdempotentDecomposition](/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/)
- Source path: [`TauLib/BookII/Regularity/IdempotentDecomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L99-L102)
- Source range: L99-L102
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `II.L07` — Idempotent Decomposition Lemma

## Immediate Comment / Docstring

```lean
/-- [II.L07] Idempotent Decomposition Lemma (formal):
    e₊ · bp + e₋ · bp = bp for all sector pairs bp.

    This is the fundamental decomposition: every element of the
    bipolar spectral algebra decomposes uniquely into B-channel
    and C-channel components, and the sum recovers the original. -/
```

## Source Excerpt

```lean
theorem decompose_recovery (bp : SectorPair) :
    SectorPair.add (proj_plus bp) (proj_minus bp) = bp := by
  simp [proj_plus, proj_minus, SectorPair.add, SectorPair.mul,
        e_plus_sector, e_minus_sector]
```
