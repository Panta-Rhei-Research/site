---
{
  "projection_kind": "taulib_declaration",
  "title": "coeff_list_getD",
  "permalink": "/verify/taulib/docs/book-i-polarity-inverse-limit/coeff-list-get-d/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.InverseLimit`.",
  "declaration_id": "TauLib.BookI.Polarity.InverseLimit::coeff_list_getD",
  "declaration_slug": "coeff-list-get-d",
  "kind": "theorem",
  "name": "coeff_list_getD",
  "module_name": "TauLib.BookI.Polarity.InverseLimit",
  "module_url": "/verify/taulib/docs/book-i-polarity-inverse-limit/",
  "source_line_start": 132,
  "source_line_end": 150,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L132-L150",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L132-L150",
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
- Source path: [`TauLib/BookI/Polarity/InverseLimit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L132-L150)
- Source range: L132-L150
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
private theorem coeff_list_getD (f : TauIdx → TauIdx) (d i : TauIdx)
    (hi : i < d) : (coeff_list f d).getD i 0 = f (i + 1) := by
  rw [getD_eq_getElem' _ _ _ (by rw [coeff_list_length]; exact hi)]
  -- Goal: (coeff_list f d)[i] = f (i + 1)
  induction d generalizing i with
  | zero =>
    -- i < 0 is impossible (Nat); the goal is unreachable
    exact absurd hi (Nat.not_lt_zero i)
  | succ d' ih =>
    simp only [coeff_list]
    by_cases hi' : i < d'
    · -- i in the prefix
      rw [List.getElem_append_left (by rw [coeff_list_length]; exact hi')]
      exact ih i hi'
    · -- i = d', trailing singleton
      have hid : i = d' := by simp only [TauIdx] at *; omega
      subst hid
      rw [List.getElem_append_right (by simp [coeff_list_length])]
      simp [coeff_list_length]
```
