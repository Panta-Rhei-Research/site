---
{
  "projection_kind": "taulib_declaration",
  "title": "nat_to_inverse_limit_inj_componentwise",
  "permalink": "/verify/taulib/docs/book-i-polarity-inverse-limit/nat-to-inverse-limit-inj-componentwise/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.InverseLimit`.",
  "declaration_id": "TauLib.BookI.Polarity.InverseLimit::nat_to_inverse_limit_inj_componentwise",
  "declaration_slug": "nat-to-inverse-limit-inj-componentwise",
  "kind": "theorem",
  "name": "nat_to_inverse_limit_inj_componentwise",
  "module_name": "TauLib.BookI.Polarity.InverseLimit",
  "module_url": "/verify/taulib/docs/book-i-polarity-inverse-limit/",
  "source_line_start": 226,
  "source_line_end": 233,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L226-L233",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.InverseLimit",
        "url": "/verify/taulib/docs/book-i-polarity-inverse-limit/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L226-L233",
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

- Module: [TauLib.BookI.Polarity.InverseLimit](/verify/taulib/docs/book-i-polarity-inverse-limit/)
- Source path: [`TauLib/BookI/Polarity/InverseLimit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L226-L233)
- Source range: L226-L233
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Two natural numbers with the same canonical inverse-limit
    embedding agree on every primorial residue.  Combined with
    primorial unboundedness, this forces equality of the natural
    numbers themselves (deferred to a follow-on lemma using
    `tetration_unbounded` from `Coordinates/TowerAtoms.lean`). -/
```

## Source Excerpt

```lean
theorem nat_to_inverse_limit_inj_componentwise
    (n m : TauIdx)
    (h : ∀ k, (nat_to_inverse_limit n).coeff k = (nat_to_inverse_limit m).coeff k) :
    ∀ k, reduce n k = reduce m k := by
  intro k
  exact h k

end Tau.Polarity
```
