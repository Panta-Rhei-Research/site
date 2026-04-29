---
{
  "projection_kind": "taulib_declaration",
  "title": "minimal_alphabet",
  "permalink": "/verify/taulib/docs/book-i-orbit-saturation/minimal-alphabet/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Saturation`.",
  "declaration_id": "TauLib.BookI.Orbit.Saturation::minimal_alphabet",
  "declaration_slug": "minimal-alphabet",
  "kind": "theorem",
  "name": "minimal_alphabet",
  "module_name": "TauLib.BookI.Orbit.Saturation",
  "module_url": "/verify/taulib/docs/book-i-orbit-saturation/",
  "source_line_start": 146,
  "source_line_end": 163,
  "registry_ids": [
    "I.T09"
  ],
  "related_registry_items": [
    {
      "id": "I.T09",
      "title": "FTA on tau-Idx",
      "url": "/registry/object/I.T09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L146-L163",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Saturation",
        "url": "/verify/taulib/docs/book-i-orbit-saturation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L146-L163",
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

- Module: [TauLib.BookI.Orbit.Saturation](/verify/taulib/docs/book-i-orbit-saturation/)
- Source path: [`TauLib/BookI/Orbit/Saturation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Saturation.lean#L146-L163)
- Source range: L146-L163
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T09` — FTA on tau-Idx

## Immediate Comment / Docstring

```lean
/-- [I.T09] **The Minimal Alphabet Theorem**:
    5 generators is the unique cardinality achieving all three properties:

    **(a) Completeness**: All rewiring levels through exponentiation
    have canonical orbit channel assignments (π↔+, γ↔×, η↔^).

    **(b) Rigidity**: No non-trivial ρ-automorphism exists.
    (4 generators also have this, but 6 do not.)

    **(c) Saturation**: Tetration (level 4) has no channel,
    and is algebraically degraded (non-commutative, non-associative,
    no left identity).

    Moreover, the counter-models show:
    - **4 generators FAIL completeness**: exponentiation loses its channel
      (only 2 solenoidal generators for 3 rewiring levels)
    - **6 generators FAIL rigidity**: the swap η↔ζ is a non-trivial
      ρ-automorphism (surplus solenoidal generator creates ambiguity)

    This establishes |Gen| = 5 as the *unique* solution to the
    simultaneous requirements of completeness + rigidity + saturation. -/
```

## Source Excerpt

```lean
theorem minimal_alphabet :
    -- (a) 5 generators satisfy the spec
    MinimalAlphabetSpec ∧
    -- (b) 6 generators break rigidity
    (∃ (f : Obj6 → Obj6),
      (∀ x, f (rho6 x) = rho6 (f x)) ∧
      (∀ x, f (f x) = x) ∧
      ¬(∀ x, f x = x)) ∧
    -- (c) 4 generators break completeness
    (ladder4Channel .exp_level = none) ∧
    -- (d) Tetration is algebraically degraded
    AlgebraicDegradation :=
  ⟨five_gen_spec,
   six_gen_rigidity_fails,
   four_gen_exp_no_channel,
   tetration_algebraic_degradation⟩

end Tau.Orbit.Saturation
```
