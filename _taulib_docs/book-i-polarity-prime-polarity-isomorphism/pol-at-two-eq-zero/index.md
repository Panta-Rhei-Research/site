---
{
  "projection_kind": "taulib_declaration",
  "title": "Pol_at_two_eq_zero",
  "permalink": "/verify/taulib/docs/book-i-polarity-prime-polarity-isomorphism/pol-at-two-eq-zero/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.PrimePolarityIsomorphism`.",
  "declaration_id": "TauLib.BookI.Polarity.PrimePolarityIsomorphism::Pol_at_two_eq_zero",
  "declaration_slug": "pol-at-two-eq-zero",
  "kind": "theorem",
  "name": "Pol_at_two_eq_zero",
  "module_name": "TauLib.BookI.Polarity.PrimePolarityIsomorphism",
  "module_url": "/verify/taulib/docs/book-i-polarity-prime-polarity-isomorphism/",
  "source_line_start": 113,
  "source_line_end": 116,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean#L113-L116",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.PrimePolarityIsomorphism",
        "url": "/verify/taulib/docs/book-i-polarity-prime-polarity-isomorphism/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean#L113-L116",
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

- Module: [TauLib.BookI.Polarity.PrimePolarityIsomorphism](/verify/taulib/docs/book-i-polarity-prime-polarity-isomorphism/)
- Source path: [`TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean#L113-L116)
- Source range: L113-L116
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Pol at p = 2 returns X (= 0)** (paper Def 5.1 X-class clause). -/
```

## Source Excerpt

```lean
theorem Pol_at_two_eq_zero : Pol 2 = 0 := by
  unfold Pol
  -- chi_p 2 2 = 0 (since 2 is even, Kronecker convention)
  native_decide
```
