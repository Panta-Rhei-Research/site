---
{
  "projection_kind": "taulib_declaration",
  "title": "categoricity_non_omega",
  "permalink": "/verify/taulib/docs/book-i-orbit-rigidity/categoricity-non-omega/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Rigidity`.",
  "declaration_id": "TauLib.BookI.Orbit.Rigidity::categoricity_non_omega",
  "declaration_slug": "categoricity-non-omega",
  "kind": "theorem",
  "name": "categoricity_non_omega",
  "module_name": "TauLib.BookI.Orbit.Rigidity",
  "module_url": "/verify/taulib/docs/book-i-orbit-rigidity/",
  "source_line_start": 153,
  "source_line_end": 166,
  "registry_ids": [
    "I.T08"
  ],
  "related_registry_items": [
    {
      "id": "I.T08",
      "title": "Categoricity of tau_0",
      "url": "/registry/object/I.T08/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L153-L166",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Rigidity",
        "url": "/verify/taulib/docs/book-i-orbit-rigidity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L153-L166",
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

- Module: [TauLib.BookI.Orbit.Rigidity](/verify/taulib/docs/book-i-orbit-rigidity/)
- Source path: [`TauLib/BookI/Orbit/Rigidity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L153-L166)
- Source range: L153-L166
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T08` — Categoricity of tau_0

## Immediate Comment / Docstring

```lean
/-- [I.T08] **Categoricity** (non-omega): unique homomorphism into any model. -/
```

## Source Excerpt

```lean
theorem categoricity_non_omega (M : TauModel)
    (f : TauObj → M.Carrier)
    (f_gen : ∀ g, f (TauObj.ofGen g) = M.gen g)
    (f_rho : ∀ x, f (rho x) = M.rho_model (f x))
    (g : Generator) (hg : g ≠ omega) (n : Nat) :
    f ⟨g, n⟩ = interpret M ⟨g, n⟩ := by
  induction n with
  | zero => simp [interpret, TauObj.ofGen] at f_gen ⊢; exact f_gen g
  | succ n ih =>
    have h_rho := f_rho ⟨g, n⟩
    rw [K4_no_jump g hg n] at h_rho
    rw [h_rho, ih]; simp [interpret]

end Tau.Orbit
```
