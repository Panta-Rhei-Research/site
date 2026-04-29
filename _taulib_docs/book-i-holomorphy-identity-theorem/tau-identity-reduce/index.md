---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_identity_reduce",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/tau-identity-reduce/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.IdentityTheorem`.",
  "declaration_id": "TauLib.BookI.Holomorphy.IdentityTheorem::tau_identity_reduce",
  "declaration_slug": "tau-identity-reduce",
  "kind": "theorem",
  "name": "tau_identity_reduce",
  "module_name": "TauLib.BookI.Holomorphy.IdentityTheorem",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/",
  "source_line_start": 118,
  "source_line_end": 125,
  "registry_ids": [
    "I.T21"
  ],
  "related_registry_items": [
    {
      "id": "I.T21",
      "title": "Tau-Identity Theorem",
      "url": "/registry/object/I.T21/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L118-L125",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.IdentityTheorem",
        "url": "/verify/taulib/docs/book-i-holomorphy-identity-theorem/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L118-L125",
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

- Module: [TauLib.BookI.Holomorphy.IdentityTheorem](/verify/taulib/docs/book-i-holomorphy-identity-theorem/)
- Source path: [`TauLib/BookI/Holomorphy/IdentityTheorem.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/IdentityTheorem.lean#L118-L125)
- Source range: L118-L125
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T21` — Tau-Identity Theorem

## Immediate Comment / Docstring

```lean
/-- [I.T21] The τ-Identity Theorem (stagewise form):
    If two tower-coherent "reduce-form" stagewise functions have the same
    underlying maps, they produce the same outputs at every stage.

    This is trivially true by definition, but it captures the KEY insight:
    a reduce-form function is uniquely determined by its underlying map.
    Tower coherence + reduce form = complete determination. -/
```

## Source Excerpt

```lean
theorem tau_identity_reduce (f₁ f₂ : StageFun)
    (rf₁ : ReduceForm f₁) (rf₂ : ReduceForm f₂)
    (hb : rf₁.b_map = rf₂.b_map) (hc : rf₁.c_map = rf₂.c_map) :
    ∀ n k, agree_at f₁ f₂ n k := by
  intro n k
  constructor
  · rw [rf₁.b_eq, rf₂.b_eq, hb]
  · rw [rf₁.c_eq, rf₂.c_eq, hc]
```
