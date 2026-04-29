---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_tau_classifier",
  "permalink": "/verify/taulib/docs/book-i-topos-earned-topos/omega-tau-classifier/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.EarnedTopos`.",
  "declaration_id": "TauLib.BookI.Topos.EarnedTopos::omega_tau_classifier",
  "declaration_slug": "omega-tau-classifier",
  "kind": "theorem",
  "name": "omega_tau_classifier",
  "module_name": "TauLib.BookI.Topos.EarnedTopos",
  "module_url": "/verify/taulib/docs/book-i-topos-earned-topos/",
  "source_line_start": 55,
  "source_line_end": 58,
  "registry_ids": [
    "I.T25"
  ],
  "related_registry_items": [
    {
      "id": "I.T25",
      "title": "Omega_tau Subobject Classifier",
      "url": "/registry/object/I.T25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L55-L58",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.EarnedTopos",
        "url": "/verify/taulib/docs/book-i-topos-earned-topos/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L55-L58",
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

- Module: [TauLib.BookI.Topos.EarnedTopos](/verify/taulib/docs/book-i-topos-earned-topos/)
- Source path: [`TauLib/BookI/Topos/EarnedTopos.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L55-L58)
- Source range: L55-L58
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.T25` — Omega_tau Subobject Classifier

## Immediate Comment / Docstring

```lean
/-- [I.T25] The subobject classifier for PSh(Cat_τ) is Ω_τ = Truth4.

    In a Grothendieck topos, the subobject classifier Ω is characterized by:
    for every mono m: S ↪ X, there exists a unique χ: X → Ω such that
    the pullback of true: 1 → Ω along χ recovers S.

    In our four-valued setting:
    - T: the element is in S (both sectors confirm membership)
    - F: the element is not in S (both sectors deny)
    - B: overdetermined (B-sector confirms, C-sector denies)
    - N: underdetermined (neither sector confirms)

    The key theorem: Ω_τ has exactly four elements, matching Truth4. -/
```

## Source Excerpt

```lean
theorem omega_tau_classifier :
    (∀ v : Omega_tau, v = T ∨ v = F ∨ v = B ∨ v = N) := by
  intro v
  cases v <;> simp
```
