---
{
  "projection_kind": "taulib_declaration",
  "title": "c_tau_eq_one",
  "permalink": "/verify/taulib/docs/book-i-denotation-solenoid-pitch/c-tau-eq-one/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Denotation.SolenoidPitch`.",
  "declaration_id": "TauLib.BookI.Denotation.SolenoidPitch::c_tau_eq_one",
  "declaration_slug": "c-tau-eq-one",
  "kind": "theorem",
  "name": "c_tau_eq_one",
  "module_name": "TauLib.BookI.Denotation.SolenoidPitch",
  "module_url": "/verify/taulib/docs/book-i-denotation-solenoid-pitch/",
  "source_line_start": 132,
  "source_line_end": 140,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/SolenoidPitch.lean#L132-L140",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.SolenoidPitch",
        "url": "/verify/taulib/docs/book-i-denotation-solenoid-pitch/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/SolenoidPitch.lean#L132-L140",
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

- Module: [TauLib.BookI.Denotation.SolenoidPitch](/verify/taulib/docs/book-i-denotation-solenoid-pitch/)
- Source path: [`TauLib/BookI/Denotation/SolenoidPitch.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/SolenoidPitch.lean#L132-L140)
- Source range: L132-L140
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **c_τ = 1 (Solenoid Pitch Theorem).**

    The solenoid pitch c_τ = dπ/dα equals 1. Encoded as:
    for all n, the depth of RT_α(n) equals the depth of RT_π(n),
    AND neither orbit can be reparametrized (Aut(τ) = {id}).

    **Proof:**
    - depth_sync gives RT_α(n).depth = RT_π(n).depth = n for all n.
    - rigidity_non_omega eliminates any automorphism that could
      rescale one orbit relative to the other.
    - Therefore the advance ratio dπ/dα = 1 is a structural invariant,
      not a gauge artifact.

    **Physical bridge (not formalized here):**
    Step 5 of the proof chain uses j² = +1 (I.T10) to show that the
    split-complex structure forces a hyperbolic (wave-type) transport
    equation whose null speed in these coordinates equals the solenoid
    pitch = 1. See BipolarAlgebra.lean for j² = +1. -/
```

## Source Excerpt

```lean
theorem c_tau_eq_one :
    -- (1) Depth synchronization: all orbits advance at the same rate
    (∀ n : TauIdx, (RT alpha n).depth = (RT pi n).depth) ∧
    -- (2) No reparametrization freedom: any automorphism preserving
    --     seeds acts as the identity (rigidity)
    (∀ (φ : TauAutomorphism) (g : Generator) (hg : g ≠ omega)
       (h_seed : (φ.toFun ⟨g, 0⟩).seed = g) (n : Nat),
       φ.toFun ⟨g, n⟩ = ⟨g, n⟩) := by
  exact ⟨pitch_ratio_one, rigidity_non_omega⟩
```
