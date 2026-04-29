---
{
  "projection_kind": "taulib_declaration",
  "title": "truncate_compat",
  "permalink": "/verify/taulib/docs/book-i-polarity-inverse-limit/truncate-compat/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.InverseLimit`.",
  "declaration_id": "TauLib.BookI.Polarity.InverseLimit::truncate_compat",
  "declaration_slug": "truncate-compat",
  "kind": "theorem",
  "name": "truncate_compat",
  "module_name": "TauLib.BookI.Polarity.InverseLimit",
  "module_url": "/verify/taulib/docs/book-i-polarity-inverse-limit/",
  "source_line_start": 171,
  "source_line_end": 184,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L171-L184",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L171-L184",
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
- Source path: [`TauLib/BookI/Polarity/InverseLimit.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/InverseLimit.lean#L171-L184)
- Source range: L171-L184
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The truncation of an inverse-limit tower is `Compatible` at the
    depth-truncated level (lifting from the `compat` hypothesis to
    the `Compatible` predicate). -/
```

## Source Excerpt

```lean
theorem truncate_compat (t : OmegaInverseLimit) (d : TauIdx) :
    Compatible (t.truncate d) := by
  intro k l hk hkl hld
  dsimp only [OmegaInverseLimit.truncate, Compatible] at *
  have hl : l - 1 < d := by simp only [TauIdx] at *; omega
  have hk' : k - 1 < d := by simp only [TauIdx] at *; omega
  -- After dsimp, components have unfolded to `coeff_list t.coeff d`
  rw [coeff_list_getD t.coeff d (l - 1) hl,
      coeff_list_getD t.coeff d (k - 1) hk']
  -- Goal: t.coeff (l - 1 + 1) % primorial k = t.coeff (k - 1 + 1)
  have hl1 : l - 1 + 1 = l := by simp only [TauIdx] at *; omega
  have hk1 : k - 1 + 1 = k := by simp only [TauIdx] at *; omega
  rw [hl1, hk1]
  exact t.compat k l hk hkl
```
