---
{
  "projection_kind": "taulib_declaration",
  "title": "diverge_go_comm",
  "permalink": "/corpus/taulib/docs/book-i-polarity-omega-germs/diverge-go-comm/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.OmegaGerms`.",
  "declaration_id": "TauLib.BookI.Polarity.OmegaGerms::diverge_go_comm",
  "declaration_slug": "diverge-go-comm",
  "kind": "theorem",
  "name": "diverge_go_comm",
  "module_name": "TauLib.BookI.Polarity.OmegaGerms",
  "module_url": "/corpus/taulib/docs/book-i-polarity-omega-germs/",
  "source_line_start": 219,
  "source_line_end": 234,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L219-L234",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.OmegaGerms",
        "url": "/corpus/taulib/docs/book-i-polarity-omega-germs/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L219-L234",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Polarity.OmegaGerms](/corpus/taulib/docs/book-i-polarity-omega-germs/)
- Source path: [`TauLib/BookI/Polarity/OmegaGerms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaGerms.lean#L219-L234)
- Source range: L219-L234
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Helper: diverge_go is symmetric in its list arguments. -/
```

## Source Excerpt

```lean
private theorem diverge_go_comm (c1 c2 : List TauIdx) (d i fuel : Nat) :
    diverge_go c1 c2 d i fuel = diverge_go c2 c1 d i fuel := by
  induction fuel generalizing i with
  | zero => unfold diverge_go; rfl
  | succ n ih =>
    unfold diverge_go
    simp only [Nat.succ_ne_zero, ↓reduceIte]
    split
    · rfl
    · -- Case split on equality of components
      by_cases h : List.getD c1 i 0 = List.getD c2 i 0
      · -- Equal: both bne checks false, recurse via IH
        simp_all
      · -- Unequal: both bne checks true, both return i + 1
        have h' : List.getD c2 i 0 ≠ List.getD c1 i 0 := Ne.symm h
        simp_all
```
