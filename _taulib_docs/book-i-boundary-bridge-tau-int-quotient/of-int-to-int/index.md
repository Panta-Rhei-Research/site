---
{
  "projection_kind": "taulib_declaration",
  "title": "TauIntQ.ofInt_toInt",
  "permalink": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/of-int-to-int/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Bridge.TauIntQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauIntQuotient::TauIntQ.ofInt_toInt",
  "declaration_slug": "of-int-to-int",
  "kind": "theorem",
  "name": "TauIntQ.ofInt_toInt",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauIntQuotient",
  "module_url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/",
  "source_line_start": 284,
  "source_line_end": 295,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L284-L295",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauIntQuotient",
        "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L284-L295",
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

- Module: [TauLib.BookI.Boundary.Bridge.TauIntQuotient](/corpus/taulib/docs/book-i-boundary-bridge-tau-int-quotient/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L284-L295)
- Source range: L284-L295
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem TauIntQ.ofInt_toInt (n : Int) : (TauIntQ.ofInt n).toInt = n := by
  unfold TauIntQ.ofInt
  by_cases h : n ≥ 0
  · simp only [h, ↓reduceDIte, TauIntQ.toInt_mk, TauInt.toInt]
    push_cast
    omega
  · push_neg at h
    have hneg : -n ≥ 0 := by omega
    have hcast : ((-n).toNat : Int) = -n := Int.toNat_of_nonneg hneg
    simp only [show ¬ n ≥ 0 from not_le.mpr h, ↓reduceDIte, TauIntQ.toInt_mk, TauInt.toInt]
    push_cast
    omega
```
