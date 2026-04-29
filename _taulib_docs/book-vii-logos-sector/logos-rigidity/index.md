---
{
  "projection_kind": "taulib_declaration",
  "title": "logos_rigidity",
  "permalink": "/verify/taulib/docs/book-vii-logos-sector/logos-rigidity/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Logos.Sector`.",
  "declaration_id": "TauLib.BookVII.Logos.Sector::logos_rigidity",
  "declaration_slug": "logos-rigidity",
  "kind": "theorem",
  "name": "logos_rigidity",
  "module_name": "TauLib.BookVII.Logos.Sector",
  "module_url": "/verify/taulib/docs/book-vii-logos-sector/",
  "source_line_start": 479,
  "source_line_end": 487,
  "registry_ids": [
    "VII.L16"
  ],
  "related_registry_items": [
    {
      "id": "VII.L16",
      "title": "Register Preservation",
      "url": "/registry/object/VII.L16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L479-L487",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L479-L487",
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

- Module: [TauLib.BookVII.Logos.Sector](/verify/taulib/docs/book-vii-logos-sector/)
- Source path: [`TauLib/BookVII/Logos/Sector.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Logos/Sector.lean#L479-L487)
- Source range: L479-L487
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.L16` — Register Preservation

## Immediate Comment / Docstring

```lean
/-- [VII.L16] Logos Rigidity (ch120). For φ ∈ S_D \ S_L, exactly one holds:
    (i) Bridge undefined (provable but not commitment-eligible)
    (ii) Bridge not faithful (distinct proofs collapse to same stance)
    (iii) Bridge not full (commitment structure not captured by any proof)

    Register identity is preserved everywhere except at S_L.

    Proof: follows from register rigidity (VII.T04) — re-typing content
    between sectors changes the normaliser verdict. If φ ∈ S_D \ S_L,
    then N_C(φ, w') ≠ accept for any Reg_C-witness w'. -/
```

## Source Excerpt

```lean
theorem logos_rigidity :
    -- Sector structure preserved
    canonical_sector_decomp.sector_count = 5 ∧
    -- D-C coincidence only at S_L
    sector_logos.dc_coincidence = true ∧
    sector_logos.unique_mediator = true ∧
    -- Rigidity from VII.T04
    canonical_sector_decomp.pure_sector_count = 4 :=
  ⟨rfl, rfl, rfl, rfl⟩
```
