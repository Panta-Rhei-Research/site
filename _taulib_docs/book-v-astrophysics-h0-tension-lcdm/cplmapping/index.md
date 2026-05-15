---
{
  "projection_kind": "taulib_declaration",
  "title": "CPLMapping",
  "permalink": "/corpus/taulib/docs/book-v-astrophysics-h0-tension-lcdm/cplmapping/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Astrophysics.H0TensionLCDM`.",
  "declaration_id": "TauLib.BookV.Astrophysics.H0TensionLCDM::CPLMapping",
  "declaration_slug": "cplmapping",
  "kind": "structure",
  "name": "CPLMapping",
  "module_name": "TauLib.BookV.Astrophysics.H0TensionLCDM",
  "module_url": "/corpus/taulib/docs/book-v-astrophysics-h0-tension-lcdm/",
  "source_line_start": 314,
  "source_line_end": 327,
  "registry_ids": [
    "V.D295"
  ],
  "related_registry_items": [
    {
      "id": "V.D295",
      "title": "CPL Mapping of τ-EoS",
      "url": "/registry/object/V.D295/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L314-L327",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.H0TensionLCDM",
        "url": "/corpus/taulib/docs/book-v-astrophysics-h0-tension-lcdm/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L314-L327",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookV.Astrophysics.H0TensionLCDM](/corpus/taulib/docs/book-v-astrophysics-h0-tension-lcdm/)
- Source path: [`TauLib/BookV/Astrophysics/H0TensionLCDM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/H0TensionLCDM.lean#L314-L327)
- Source range: L314-L327
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- `V.D295` — CPL Mapping of τ-EoS

## Immediate Comment / Docstring

```lean
/-- [V.D295] CPL mapping of τ-EoS:
    w(z) = w₀ + wₐ · z/(1+z).
    w₀ = ι_τ³ − 1 ≈ −0.960, wₐ > 0 (defects deplete → w approaches −1).

    DESI DR2 (2025): w₀ = −0.75 ± 0.11, wₐ = −0.99 ± 0.48.
    τ-tension with DESI: ~2σ. τ is closer to DESI than ΛCDM on w₀. -/
```

## Source Excerpt

```lean
structure CPLMapping where
  /-- w₀ offset from −1 (×1000): ι_τ³ ≈ 0.040 → 40. -/
  w0_offset_x1000 : Nat
  /-- wₐ sign: positive (defect depletion). -/
  wa_positive : Bool := true
  /-- DESI w₀ central (×1000, offset from −1): 0.25 → 250. -/
  desi_w0_offset_x1000 : Nat := 250
  /-- DESI w₀ uncertainty (×1000): 0.11 → 110. -/
  desi_w0_unc_x1000 : Nat := 110
  /-- DESI wₐ central (×1000): −0.99 → negative. -/
  desi_wa_x1000 : Int := -990
  /-- Tension with DESI (×10 σ): ~2σ → 20. -/
  desi_tension_x10sigma : Nat
  deriving Repr
```
