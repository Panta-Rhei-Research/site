---
{
  "projection_kind": "taulib_declaration",
  "title": "eval at L285",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/eval-l285/",
  "summary_short": "`eval` declaration in `TauLib.BookV.Astrophysics.SectorExhaustion`.",
  "declaration_id": "TauLib.BookV.Astrophysics.SectorExhaustion::#eval:285",
  "declaration_slug": "eval-l285",
  "kind": "eval",
  "name": null,
  "module_name": "TauLib.BookV.Astrophysics.SectorExhaustion",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/",
  "source_line_start": 285,
  "source_line_end": 285,
  "registry_ids": [
    "V.R202",
    "V.R203",
    "V.R204"
  ],
  "related_registry_items": [
    {
      "id": "V.R202",
      "title": "Minimal Alphabet and Sector Count",
      "url": "/registry/object/V.R202/"
    },
    {
      "id": "V.R203",
      "title": "From \"Not Needed\" to \"Not Possible\"",
      "url": "/registry/object/V.R203/"
    },
    {
      "id": "V.R204",
      "title": "What 68% and 27% Actually Are",
      "url": "/registry/object/V.R204/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L285-L285",
  "formal_status": "computed",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.SectorExhaustion",
        "url": "/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L285-L285",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "eval",
      "status": "computed"
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

- Module: [TauLib.BookV.Astrophysics.SectorExhaustion](/verify/taulib/docs/book-v-astrophysics-sector-exhaustion/)
- Source path: [`TauLib/BookV/Astrophysics/SectorExhaustion.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/SectorExhaustion.lean#L285-L285)
- Source range: L285-L285
- Kind: `eval`
- Formal status hint: `computed`

## Registry Links

- `V.R202` — Minimal Alphabet and Sector Count
- `V.R203` — From "Not Needed" to "Not Possible"
- `V.R204` — What 68% and 27% Actually Are

## Immediate Comment / Docstring

```lean
-- ============================================================
-- REMARKS (comment-only)
-- ============================================================

-- [V.R202] Every Astrophysical Phenomenon Maps to Sectors: this is
-- the astrophysical analog of the force completeness proven in
-- Book III. Where Book III proves completeness for particle physics,
-- Book V demonstrates it for astrophysics.

-- [V.R203] No Sixth Force: the τ-framework's 5 generators yield
-- exactly 5 sectors. A sixth force would require a sixth generator,
-- which contradicts the minimal alphabet theorem (Book I, I.L05).

-- [V.R204] Dark Matter and Dark Energy Unnecessary: "dark matter"
-- is the boundary holonomy correction; "dark energy" is the
-- cosmological constant artifact (Book V ch22). Neither requires
-- new particles or fields beyond the 5 sectors.

-- ============================================================
-- SMOKE TESTS
-- ============================================================
```

## Source Excerpt

```lean
#eval (primarySectors .GravitationalDynamics).length  -- 1
```
