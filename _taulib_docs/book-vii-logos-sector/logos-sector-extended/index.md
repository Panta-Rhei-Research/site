---
{
  "projection_kind": "taulib_declaration",
  "title": "LogosSectorExtended",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/logos-sector-extended/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::LogosSectorExtended",
  "declaration_slug": "logos-sector-extended",
  "kind": "structure",
  "name": "LogosSectorExtended",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 357,
  "source_line_end": 366,
  "registry_ids": [
    "VII.D86"
  ],
  "related_registry_items": [
    {
      "id": "VII.D86",
      "title": "Logos Sector",
      "url": "/registry/object/VII.D86/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L357-L366",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Logos.Sector",
        "url": "/verify/taulib/docs/book-vii-logos-sector/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L357-L366",
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

- Module: [TauLib.BookVII.Logos.Sector](/verify/taulib/docs/book-vii-logos-sector/)
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L357-L366)
- Source range: L357-L366
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.D86` — Logos Sector

## Immediate Comment / Docstring

```lean
/-- [VII.D86] Logos Sector (Extended, ch119).
    S_L = S_D ∩ S_C, equipped with the coincidence property:
    φ is S_L-admissible iff:
    (i) Reg_D-valid (derivable from 7 axioms + 5 generators)
    (ii) Reg_C-stable (agent can coherently live it)
    (iii) Mutual witnessing: the Reg_D-proof IS the Reg_C-ground, and vice versa -/
```

## Source Excerpt

```lean
structure LogosSectorExtended where
  /-- D-C coincidence: proof-validity = stance-stability. -/
  dc_coincidence : Bool := true
  /-- Proof and stance are the same structural datum. -/
  proof_stance_identity : Bool := true
  /-- Mutual witnessing: D-proof is C-ground. -/
  mutual_witnessing : Bool := true
  /-- Terminal in category of coincidence sectors. -/
  terminal : Bool := true
  deriving Repr
```
