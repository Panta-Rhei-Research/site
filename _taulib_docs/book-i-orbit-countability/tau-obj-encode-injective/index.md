---
{
  "projection_kind": "taulib_declaration",
  "title": "tauObj_encode_injective",
  "permalink": "/verify/taulib/docs/book-i-orbit-countability/tau-obj-encode-injective/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Orbit.Countability`.",
  "declaration_id": "TauLib.BookI.Orbit.Countability::tauObj_encode_injective",
  "declaration_slug": "tau-obj-encode-injective",
  "kind": "theorem",
  "name": "tauObj_encode_injective",
  "module_name": "TauLib.BookI.Orbit.Countability",
  "module_url": "/verify/taulib/docs/book-i-orbit-countability/",
  "source_line_start": 60,
  "source_line_end": 70,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Countability.lean#L60-L70",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Countability",
        "url": "/verify/taulib/docs/book-i-orbit-countability/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Countability.lean#L60-L70",
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

- Module: [TauLib.BookI.Orbit.Countability](/verify/taulib/docs/book-i-orbit-countability/)
- Source path: [`TauLib/BookI/Orbit/Countability.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Countability.lean#L60-L70)
- Source range: L60-L70
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The encoding is injective: distinct TauObjs yield distinct codes. -/
```

## Source Excerpt

```lean
theorem tauObj_encode_injective (x y : TauObj) (h : tauObj_encode x = tauObj_encode y) :
    x = y := by
  cases x with | mk sx dx =>
  cases y with | mk sy dy =>
  simp only [tauObj_encode] at h
  have h_seed_lt : sx.toNat < 5 := by cases sx <;> simp [Generator.toNat]
  have h_seed_lt2 : sy.toNat < 5 := by cases sy <;> simp [Generator.toNat]
  have h_depth : dx = dy := by omega
  have h_seed_nat : sx.toNat = sy.toNat := by omega
  subst h_depth
  cases sx <;> cases sy <;> simp_all [Generator.toNat]
```
