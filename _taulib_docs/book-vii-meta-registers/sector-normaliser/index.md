---
{
  "projection_kind": "taulib_declaration",
  "title": "SectorNormaliser",
  "permalink": "/verify/taulib/docs/book-vii-meta-registers/sector-normaliser/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::SectorNormaliser",
  "declaration_slug": "sector-normaliser",
  "kind": "structure",
  "name": "SectorNormaliser",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/verify/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 381,
  "source_line_end": 389,
  "registry_ids": [
    "VII.D14"
  ],
  "related_registry_items": [
    {
      "id": "VII.D14",
      "title": "Sector Normaliser",
      "url": "/registry/object/VII.D14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L381-L389",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/verify/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L381-L389",
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

- Module: [TauLib.BookVII.Meta.Registers](/verify/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L381-L389)
- Source range: L381-L389
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D14` — Sector Normaliser

## Immediate Comment / Docstring

```lean
/-- [VII.D14] Sector Normaliser: bounded pipeline evaluating coherence verdict.
    Subject to (N1) Boundedness, (N2) Soundness, (N3) Determinism. -/
```

## Source Excerpt

```lean
structure SectorNormaliser where
  sector : SectorId
  /-- (N1) Terminates in finitely many NF-reduction steps. -/
  bounded : Bool := true
  /-- (N2) Accept ⟹ content genuinely satisfies coherence criterion. -/
  sound : Bool := true
  /-- (N3) Verdict depends only on structural content of (c,w). -/
  deterministic : Bool := true
  deriving Repr
```
