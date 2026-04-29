---
{
  "projection_kind": "taulib_declaration",
  "title": "h2_unified_classifier_synthesis",
  "permalink": "/verify/taulib/docs/book-i-polarity-prime-polarity-isomorphism/h2-unified-classifier-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.PrimePolarityIsomorphism`.",
  "declaration_id": "TauLib.BookI.Polarity.PrimePolarityIsomorphism::h2_unified_classifier_synthesis",
  "declaration_slug": "h2-unified-classifier-synthesis",
  "kind": "theorem",
  "name": "h2_unified_classifier_synthesis",
  "module_name": "TauLib.BookI.Polarity.PrimePolarityIsomorphism",
  "module_url": "/verify/taulib/docs/book-i-polarity-prime-polarity-isomorphism/",
  "source_line_start": 236,
  "source_line_end": 245,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean#L236-L245",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean#L236-L245",
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
- Source path: [`TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimePolarityIsomorphism.lean#L236-L245)
- Source range: L236-L245
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Outreach-facing structural identity**: the prime polarity
    classifier is **derived** from τ-framework first principles
    (CRT idempotents → split-complex algebra → spectral weight →
    bipolar label) and **agrees** with the orthodox Legendre-based
    classifier at every prime.

    This synthesises Wave 18's τ-derivation with paper §7's
    isomorphism, completing the H2 arc at the structural level. -/
```

## Source Excerpt

```lean
theorem h2_unified_classifier_synthesis (i : TauIdx) :
    -- Wave 18: the τ-framework classifier is labelInfty
    labelInfty i = chi_p (nth_prime (i + 1)) 2 ∧
    -- Wave 19a (this PR): orthodox classifier coincides
    Pol (nth_prime (i + 1)) = labelInfty i ∧
    -- The two classifiers agree pointwise
    unifiedClassifier i = Pol (nth_prime (i + 1)) :=
  ⟨rfl, rfl, rfl⟩

end Tau.Polarity
```
