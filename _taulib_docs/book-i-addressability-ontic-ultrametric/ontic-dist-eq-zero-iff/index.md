---
{
  "projection_kind": "taulib_declaration",
  "title": "OnticDist_eq_zero_iff",
  "permalink": "/verify/taulib/docs/book-i-addressability-ontic-ultrametric/ontic-dist-eq-zero-iff/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Addressability.OnticUltrametric`.",
  "declaration_id": "TauLib.BookI.Addressability.OnticUltrametric::OnticDist_eq_zero_iff",
  "declaration_slug": "ontic-dist-eq-zero-iff",
  "kind": "theorem",
  "name": "OnticDist_eq_zero_iff",
  "module_name": "TauLib.BookI.Addressability.OnticUltrametric",
  "module_url": "/verify/taulib/docs/book-i-addressability-ontic-ultrametric/",
  "source_line_start": 124,
  "source_line_end": 132,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/OnticUltrametric.lean#L124-L132",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Addressability.OnticUltrametric",
        "url": "/verify/taulib/docs/book-i-addressability-ontic-ultrametric/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/OnticUltrametric.lean#L124-L132",
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

- Module: [TauLib.BookI.Addressability.OnticUltrametric](/verify/taulib/docs/book-i-addressability-ontic-ultrametric/)
- Source path: [`TauLib/BookI/Addressability/OnticUltrametric.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/OnticUltrametric.lean#L124-L132)
- Source range: L124-L132
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `OnticDist = 0` iff the two NFs are NF-equivalent (same ρ-count
    and pointwise-equal seed maps). -/
```

## Source Excerpt

```lean
theorem OnticDist_eq_zero_iff (nf₁ nf₂ : NormalForm) :
    OnticDist nf₁ nf₂ = 0 ↔ nfEquiv nf₁ nf₂ := by
  unfold OnticDist
  by_cases h : nfEquiv nf₁ nf₂
  · rw [if_pos h]; exact ⟨fun _ => h, fun _ => rfl⟩
  · rw [if_neg h]
    constructor
    · intro h_zero; exact absurd h_zero (by omega)
    · intro h'; exact absurd h' h
```
