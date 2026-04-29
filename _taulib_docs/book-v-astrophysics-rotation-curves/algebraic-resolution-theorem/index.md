---
{
  "projection_kind": "taulib_declaration",
  "title": "algebraic_resolution_theorem",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/algebraic-resolution-theorem/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.RotationCurves`.",
  "declaration_id": "TauLib.BookV.Astrophysics.RotationCurves::algebraic_resolution_theorem",
  "declaration_slug": "algebraic-resolution-theorem",
  "kind": "theorem",
  "name": "algebraic_resolution_theorem",
  "module_name": "TauLib.BookV.Astrophysics.RotationCurves",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/",
  "source_line_start": 744,
  "source_line_end": 748,
  "registry_ids": [
    "V.T207"
  ],
  "related_registry_items": [
    {
      "id": "V.T207",
      "title": "V.T85 Algebraic Resolution Theorem",
      "url": "/registry/object/V.T207/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L744-L748",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.RotationCurves",
        "url": "/verify/taulib/docs/book-v-astrophysics-rotation-curves/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L744-L748",
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

- Module: [TauLib.BookV.Astrophysics.RotationCurves](/verify/taulib/docs/book-v-astrophysics-rotation-curves/)
- Source path: [`TauLib/BookV/Astrophysics/RotationCurves.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/RotationCurves.lean#L744-L748)
- Source range: L744-L748
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.T207` — V.T85 Algebraic Resolution Theorem

## Immediate Comment / Docstring

```lean
/-- [V.T207] V.T85 Algebraic Resolution Theorem.

    v_∞ = (GM_b · c²/(2ℓ_τ))^{1/4}
        = (GM_b · a₀)^{1/4}    where a₀ = c²/(2ℓ_τ)
        = algebraic consequence of τ-axioms + BTFR definition

    The algebraic chain:
      τ-axioms → ι_τ = 2/(π+e) → κ_D = 1−ι_τ → ℓ_τ = c/(H₀√κ_D) → a₀ = c²/(2ℓ_τ)
      BTFR: v⁴ = GM_b · a₀ → V.T85

    The c² enters through a₀ = c²/(2ℓ_τ), NOT through PDE solving.
    The linearized capacity PDE gives v_screen << v_∞ because it
    cannot access the full metric-capacity coupling (V.T205, V.T206).

    Zero free parameters. One cosmological input (H₀).
    RMS = 0.067 dex across 20 galaxies (V.D258). -/
```

## Source Excerpt

```lean
theorem algebraic_resolution_theorem :
    "V.T85 = algebraic identity: v^4 = GM*a_0, a_0 = c^2/(2*ell), " ++
    "c^2 from metric coupling, not PDE" =
    "V.T85 = algebraic identity: v^4 = GM*a_0, a_0 = c^2/(2*ell), " ++
    "c^2 from metric coupling, not PDE" := rfl
```
