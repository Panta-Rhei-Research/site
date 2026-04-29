---
{
  "projection_kind": "taulib_declaration",
  "title": "universal_op_check",
  "permalink": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/universal-op-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.LanglandsReflection`.",
  "declaration_id": "TauLib.BookIII.Sectors.LanglandsReflection::universal_op_check",
  "declaration_slug": "universal-op-check",
  "kind": "def",
  "name": "universal_op_check",
  "module_name": "TauLib.BookIII.Sectors.LanglandsReflection",
  "module_url": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/",
  "source_line_start": 122,
  "source_line_end": 138,
  "registry_ids": [
    "III.D16"
  ],
  "related_registry_items": [
    {
      "id": "III.D16",
      "title": "Universal Operator",
      "url": "/registry/object/III.D16/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L122-L138",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Sectors.LanglandsReflection",
        "url": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L122-L138",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookIII.Sectors.LanglandsReflection](/verify/taulib/docs/book-iii-sectors-langlands-reflection/)
- Source path: [`TauLib/BookIII/Sectors/LanglandsReflection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L122-L138)
- Source range: L122-L138
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D16` — Universal Operator

## Immediate Comment / Docstring

```lean
/-- [III.D16] Universal operator is reduce-stable at each stage. -/
```

## Source Excerpt

```lean
def universal_op_check (bound db : TauIdx) : Bool :=
  go 0 1 ((bound + 1) * (db + 1))
where
  go (m k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if m > bound then true
    else if k > db then go (m + 1) 1 (fuel - 1)
    else
      let χ : BoundaryCharacter := ⟨Int.ofNat m, 0⟩
      let val := universal_operator χ 1 k bound
      let stable := reduce val k == val
      -- Also test mixed character (exercises all sectors, not just B-type)
      let χ_mixed : BoundaryCharacter := ⟨Int.ofNat m, Int.ofNat (m + 1)⟩
      let val_mixed := universal_operator χ_mixed 1 k bound
      let mixed_stable := reduce val_mixed k == val_mixed
      stable && mixed_stable && go m (k + 1) (fuel - 1)
  termination_by fuel
```
