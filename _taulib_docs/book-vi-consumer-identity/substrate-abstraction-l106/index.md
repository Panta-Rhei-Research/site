---
{
  "projection_kind": "taulib_declaration",
  "title": "substrate_abstraction",
  "permalink": "/verify/taulib/docs/book-vi-consumer-identity/substrate-abstraction-l106/",
  "summary_short": "`theorem` declaration in `TauLib.BookVI.Consumer.Identity`.",
  "declaration_id": "TauLib.BookVI.Consumer.Identity::substrate_abstraction",
  "declaration_slug": "substrate-abstraction-l106",
  "kind": "theorem",
  "name": "substrate_abstraction",
  "module_name": "TauLib.BookVI.Consumer.Identity",
  "module_url": "/verify/taulib/docs/book-vi-consumer-identity/",
  "source_line_start": 106,
  "source_line_end": 125,
  "registry_ids": [
    "VI.R29"
  ],
  "related_registry_items": [
    {
      "id": "VI.R29",
      "title": "Scope: structural, not empirical",
      "url": "/registry/object/VI.R29/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Identity.lean#L106-L125",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVI.Consumer.Identity",
        "url": "/verify/taulib/docs/book-vi-consumer-identity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Identity.lean#L106-L125",
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

- Module: [TauLib.BookVI.Consumer.Identity](/verify/taulib/docs/book-vi-consumer-identity/)
- Source path: [`TauLib/BookVI/Consumer/Identity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVI/Consumer/Identity.lean#L106-L125)
- Source range: L106-L125
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VI.R29` — Scope: structural, not empirical

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem substrate_abstraction :
    substrate_abs.conditions_abstract = true ∧
    substrate_abs.sufficient = true ∧
    substrate_abs.necessary = true ∧
    substrate_abs.substrate_independent = true :=
  ⟨rfl, rfl, rfl, rfl⟩

-- ============================================================
-- SUBSTRATE ABSTRACTION SCOPE [VI.R29]
-- ============================================================

/- [VI.R29] Scope remark: Substrate Abstraction is τ-effective because
   Distinction (VI.D04) and SelfDesc (VI.D08) are stated in terms of
   abstract morphisms in Carrier_L, not material properties. The theorem
   does not predict which physical systems will satisfy the conditions —
   that is an empirical question — but proves that the conditions themselves
   impose no substrate restriction.
   (Remark; no proof obligation) -/

end Tau.BookVI.Identity
```
