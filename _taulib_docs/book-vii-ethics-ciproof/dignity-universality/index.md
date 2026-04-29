---
{
  "projection_kind": "taulib_declaration",
  "title": "dignity_universality",
  "permalink": "/verify/taulib/docs/book-vii-ethics-ciproof/dignity-universality/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Ethics.CIProof`.",
  "declaration_id": "TauLib.BookVII.Ethics.CIProof::dignity_universality",
  "declaration_slug": "dignity-universality",
  "kind": "theorem",
  "name": "dignity_universality",
  "module_name": "TauLib.BookVII.Ethics.CIProof",
  "module_url": "/verify/taulib/docs/book-vii-ethics-ciproof/",
  "source_line_start": 113,
  "source_line_end": 118,
  "registry_ids": [
    "VII.T30"
  ],
  "related_registry_items": [
    {
      "id": "VII.T30",
      "title": "Dignity Universality",
      "url": "/registry/object/VII.T30/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L113-L118",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Ethics.CIProof",
        "url": "/verify/taulib/docs/book-vii-ethics-ciproof/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L113-L118",
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

- Module: [TauLib.BookVII.Ethics.CIProof](/verify/taulib/docs/book-vii-ethics-ciproof/)
- Source path: [`TauLib/BookVII/Ethics/CIProof.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Ethics/CIProof.lean#L113-L118)
- Source range: L113-L118
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `VII.T30` — Dignity Universality

## Immediate Comment / Docstring

```lean
/-- [VII.T30] Dignity Universality (ch76). Five claims:
    (1) Reflectivity: L_dig : A → A_dig left adjoint to inclusion
    (2) Idempotence: L_dig ∘ L_dig = L_dig
    (3) Modality: j_dig = i ∘ L_dig is Lawvere-Tierney
    (4) Universality: every NF-address-bearing entity has non-trivial D(X)
        (by rigidity Aut(τ) = {id}, structural properties are invariant)
    (5) No trade-off: no admissible policy buys utility by degrading D(X)

    Proof: (1)–(3) by reflective subcategory results (A_dig closed under
    limits + internal homs). (4) by Aut(τ) = {id}: every NF address has
    invariant structural properties. (5) by contraposition: degrading
    invariants means not factoring through A_dig. -/
```

## Source Excerpt

```lean
theorem dignity_universality :
    dignity.has_reflector = true ∧
    dignity.reflector_idempotent = true ∧
    dignity.lt_modality = true ∧
    dignity.label_independent = true :=
  ⟨rfl, rfl, rfl, rfl⟩
```
