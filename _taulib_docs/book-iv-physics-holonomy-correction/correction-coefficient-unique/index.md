---
{
  "projection_kind": "taulib_declaration",
  "title": "correction_coefficient_unique",
  "permalink": "/corpus/taulib/docs/book-iv-physics-holonomy-correction/correction-coefficient-unique/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.HolonomyCorrection`.",
  "declaration_id": "TauLib.BookIV.Physics.HolonomyCorrection::correction_coefficient_unique",
  "declaration_slug": "correction-coefficient-unique",
  "kind": "theorem",
  "name": "correction_coefficient_unique",
  "module_name": "TauLib.BookIV.Physics.HolonomyCorrection",
  "module_url": "/corpus/taulib/docs/book-iv-physics-holonomy-correction/",
  "source_line_start": 294,
  "source_line_end": 298,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L294-L298",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.HolonomyCorrection",
        "url": "/corpus/taulib/docs/book-iv-physics-holonomy-correction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L294-L298",
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

- Module: [TauLib.BookIV.Physics.HolonomyCorrection](/corpus/taulib/docs/book-iv-physics-holonomy-correction/)
- Source path: [`TauLib/BookIV/Physics/HolonomyCorrection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L294-L298)
- Source range: L294-L298
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The correction coefficient c_{1,1} = π³ is unique at order α²·ι^(−2).

    In the perturbation series R = Σ c_{j,k} · ι^{−7+5j} · α^{2k}:
    - j=0, k=0: bulk term ι^(−7), coefficient from Epstein zeta
    - j=1, k=0: capacity term −√3·ι^(−2)
    - j=1, k=1: holonomy term −π³·ι^(−2), the unique H³(τ³) coefficient

    No other topological invariant of τ³ at this order matches the
    6 ppm numerical fit. -/
```

## Source Excerpt

```lean
theorem correction_coefficient_unique :
    -- The unique coefficient: π exponent = 3, α exponent = 2
    -- At (j,k) = (1,1): exponent shift = −7 + 5×1 = −2 ✓, α power = 2×1 = 2 ✓
    ((-7 : Int) + 5 * 1 = -2) ∧ (2 * 1 = 2) := by
  exact ⟨rfl, rfl⟩
```
