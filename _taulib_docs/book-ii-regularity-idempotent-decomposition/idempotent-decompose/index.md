---
{
  "projection_kind": "taulib_declaration",
  "title": "idempotent_decompose",
  "permalink": "/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/idempotent-decompose/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.IdempotentDecomposition`.",
  "declaration_id": "TauLib.BookII.Regularity.IdempotentDecomposition::idempotent_decompose",
  "declaration_slug": "idempotent-decompose",
  "kind": "def",
  "name": "idempotent_decompose",
  "module_name": "TauLib.BookII.Regularity.IdempotentDecomposition",
  "module_url": "/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/",
  "source_line_start": 54,
  "source_line_end": 55,
  "registry_ids": [
    "II.D48"
  ],
  "related_registry_items": [
    {
      "id": "II.D48",
      "title": "Canonical Decomposition",
      "url": "/registry/object/II.D48/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L54-L55",
  "formal_status": "defined",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L54-L55",
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

- Module: [TauLib.BookII.Regularity.IdempotentDecomposition](/verify/taulib/docs/book-ii-regularity-idempotent-decomposition/)
- Source path: [`TauLib/BookII/Regularity/IdempotentDecomposition.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/IdempotentDecomposition.lean#L54-L55)
- Source range: L54-L55
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D48` — Canonical Decomposition

## Immediate Comment / Docstring

```lean
/-- [II.D48] Idempotent decomposition of a SectorPair into
    B-channel and C-channel components.

    Given bp = (B, C), returns:
    - fst = e₊ · bp = (1,0) * (B,C) = (B, 0)   [B-channel]
    - snd = e₋ · bp = (0,1) * (B,C) = (0, C)   [C-channel]

    The decomposition is canonical: determined entirely by the
    idempotent structure of the sector algebra. -/
```

## Source Excerpt

```lean
def idempotent_decompose (bp : SectorPair) : SectorPair × SectorPair :=
  (SectorPair.mul e_plus_sector bp, SectorPair.mul e_minus_sector bp)
```
