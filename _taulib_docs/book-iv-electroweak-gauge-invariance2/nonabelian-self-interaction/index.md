---
{
  "projection_kind": "taulib_declaration",
  "title": "nonabelian_self_interaction",
  "permalink": "/corpus/taulib/docs/book-iv-electroweak-gauge-invariance2/nonabelian-self-interaction/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Electroweak.GaugeInvariance2`.",
  "declaration_id": "TauLib.BookIV.Electroweak.GaugeInvariance2::nonabelian_self_interaction",
  "declaration_slug": "nonabelian-self-interaction",
  "kind": "theorem",
  "name": "nonabelian_self_interaction",
  "module_name": "TauLib.BookIV.Electroweak.GaugeInvariance2",
  "module_url": "/corpus/taulib/docs/book-iv-electroweak-gauge-invariance2/",
  "source_line_start": 247,
  "source_line_end": 251,
  "registry_ids": [
    "IV.P41"
  ],
  "related_registry_items": [
    {
      "id": "IV.P41",
      "title": "Self-Interaction from Non-Commutativity",
      "url": "/registry/object/IV.P41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L247-L251",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Electroweak.GaugeInvariance2",
        "url": "/corpus/taulib/docs/book-iv-electroweak-gauge-invariance2/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L247-L251",
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

- Module: [TauLib.BookIV.Electroweak.GaugeInvariance2](/corpus/taulib/docs/book-iv-electroweak-gauge-invariance2/)
- Source path: [`TauLib/BookIV/Electroweak/GaugeInvariance2.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Electroweak/GaugeInvariance2.lean#L247-L251)
- Source range: L247-L251
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `IV.P41` — Self-Interaction from Non-Commutativity

## Immediate Comment / Docstring

```lean
/-- [IV.P41] Non-abelian field strength has self-interaction:
    F_μν = ∂_μA_ν − ∂_νA_μ + ig[A_μ, A_ν].
    The commutator term [A_μ, A_ν] vanishes for abelian U(1). -/
```

## Source Excerpt

```lean
theorem nonabelian_self_interaction :
    gauge_su2.has_self_interaction = true ∧
    gauge_su3.has_self_interaction = true ∧
    gauge_u1.has_self_interaction = false :=
  ⟨rfl, rfl, rfl⟩
```
