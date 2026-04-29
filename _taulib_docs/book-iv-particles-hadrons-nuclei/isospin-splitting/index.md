---
{
  "projection_kind": "taulib_declaration",
  "title": "IsospinSplitting",
  "permalink": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/isospin-splitting/",
  "summary_short": "`structure` declaration in `TauLib.BookIV.Particles.HadronsNuclei`.",
  "declaration_id": "TauLib.BookIV.Particles.HadronsNuclei::IsospinSplitting",
  "declaration_slug": "isospin-splitting",
  "kind": "structure",
  "name": "IsospinSplitting",
  "module_name": "TauLib.BookIV.Particles.HadronsNuclei",
  "module_url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/",
  "source_line_start": 192,
  "source_line_end": 201,
  "registry_ids": [
    "IV.R131"
  ],
  "related_registry_items": [
    {
      "id": "IV.R131",
      "title": "Isospin splitting from polarity",
      "url": "/registry/object/IV.R131/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L192-L201",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.HadronsNuclei",
        "url": "/verify/taulib/docs/book-iv-particles-hadrons-nuclei/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L192-L201",
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

- Module: [TauLib.BookIV.Particles.HadronsNuclei](/verify/taulib/docs/book-iv-particles-hadrons-nuclei/)
- Source path: [`TauLib/BookIV/Particles/HadronsNuclei.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/HadronsNuclei.lean#L192-L201)
- Source range: L192-L201
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `IV.R131` — Isospin splitting from polarity

## Immediate Comment / Docstring

```lean
/-- [IV.R131] m_d > m_u has structural origin: the d-quark has
    η-winding n ≡ 1 mod 3 (χ₋-dominant), while u-quark has
    n ≡ 2 mod 3 (complement class). δ_A ≈ 1.293 MeV. -/
```

## Source Excerpt

```lean
structure IsospinSplitting where
  /-- d-quark winding class mod 3. -/
  d_winding_mod3 : Nat := 1
  /-- u-quark winding class mod 3. -/
  u_winding_mod3 : Nat := 2
  /-- Mass splitting (keV). -/
  delta_A_keV : Nat := 1293
  /-- d heavier than u. -/
  d_heavier : Bool := true
  deriving Repr
```
