---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_mul_list_getD",
  "permalink": "/verify/taulib/docs/book-i-polarity-omega-ring/omega-mul-list-get-d/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.OmegaRing`.",
  "declaration_id": "TauLib.BookI.Polarity.OmegaRing::omega_mul_list_getD",
  "declaration_slug": "omega-mul-list-get-d",
  "kind": "theorem",
  "name": "omega_mul_list_getD",
  "module_name": "TauLib.BookI.Polarity.OmegaRing",
  "module_url": "/verify/taulib/docs/book-i-polarity-omega-ring/",
  "source_line_start": 112,
  "source_line_end": 126,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaRing.lean#L112-L126",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.OmegaRing",
        "url": "/verify/taulib/docs/book-i-polarity-omega-ring/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaRing.lean#L112-L126",
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

- Module: [TauLib.BookI.Polarity.OmegaRing](/verify/taulib/docs/book-i-polarity-omega-ring/)
- Source path: [`TauLib/BookI/Polarity/OmegaRing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaRing.lean#L112-L126)
- Source range: L112-L126
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
private theorem omega_mul_list_getD (n1 n2 d i : Nat) (hi : i < d) :
    (omega_mul_list n1 n2 d).getD i 0 =
    (reduce n1 (i + 1) * reduce n2 (i + 1)) % primorial (i + 1) := by
  rw [getD_eq_getElem _ _ _ (by rw [omega_mul_list_length]; exact hi)]
  induction d generalizing i with
  | zero => omega
  | succ d' ih =>
    simp only [omega_mul_list]
    by_cases hi' : i < d'
    · rw [List.getElem_append_left (by rw [omega_mul_list_length]; exact hi')]
      exact ih i hi'
    · have hid : i = d' := by omega
      subst hid
      rw [List.getElem_append_right (by simp [omega_mul_list_length])]
      simp [omega_mul_list_length]
```
