---
{
  "projection_kind": "taulib_declaration",
  "title": "OnticDist_ultrametric",
  "permalink": "/verify/taulib/docs/book-i-addressability-ontic-ultrametric/ontic-dist-ultrametric/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Addressability.OnticUltrametric`.",
  "declaration_id": "TauLib.BookI.Addressability.OnticUltrametric::OnticDist_ultrametric",
  "declaration_slug": "ontic-dist-ultrametric",
  "kind": "theorem",
  "name": "OnticDist_ultrametric",
  "module_name": "TauLib.BookI.Addressability.OnticUltrametric",
  "module_url": "/verify/taulib/docs/book-i-addressability-ontic-ultrametric/",
  "source_line_start": 141,
  "source_line_end": 152,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/OnticUltrametric.lean#L141-L152",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/OnticUltrametric.lean#L141-L152",
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
- Source path: [`TauLib/BookI/Addressability/OnticUltrametric.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/OnticUltrametric.lean#L141-L152)
- Source range: L141-L152
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The **strong ultrametric inequality** —
    `OnticDist a c ≤ max (OnticDist a b) (OnticDist b c)`.

    Proof by case analysis on whether each pair is NF-equivalent.
    The only non-trivial case is when both `(a,b)` and `(b,c)` are
    equivalent — then `(a,c)` is too by transitivity, so the LHS is 0
    and the inequality holds.  Otherwise the RHS is at least 1. -/
```

## Source Excerpt

```lean
theorem OnticDist_ultrametric (nf₁ nf₂ nf₃ : NormalForm) :
    OnticDist nf₁ nf₃ ≤ max (OnticDist nf₁ nf₂) (OnticDist nf₂ nf₃) := by
  unfold OnticDist
  by_cases h12 : nfEquiv nf₁ nf₂
  · by_cases h23 : nfEquiv nf₂ nf₃
    · have h13 : nfEquiv nf₁ nf₃ := nfEquiv_trans h12 h23
      rw [if_pos h12, if_pos h23, if_pos h13]
      simp
    · rw [if_pos h12, if_neg h23]
      split <;> omega
  · rw [if_neg h12]
    split <;> omega
```
