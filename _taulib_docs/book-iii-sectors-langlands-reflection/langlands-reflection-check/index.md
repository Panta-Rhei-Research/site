---
{
  "projection_kind": "taulib_declaration",
  "title": "langlands_reflection_check",
  "permalink": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/langlands-reflection-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Sectors.LanglandsReflection`.",
  "declaration_id": "TauLib.BookIII.Sectors.LanglandsReflection::langlands_reflection_check",
  "declaration_slug": "langlands-reflection-check",
  "kind": "def",
  "name": "langlands_reflection_check",
  "module_name": "TauLib.BookIII.Sectors.LanglandsReflection",
  "module_url": "/verify/taulib/docs/book-iii-sectors-langlands-reflection/",
  "source_line_start": 50,
  "source_line_end": 74,
  "registry_ids": [
    "III.D15"
  ],
  "related_registry_items": [
    {
      "id": "III.D15",
      "title": "Langlands₁ Reflection Bridge",
      "url": "/registry/object/III.D15/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L50-L74",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L50-L74",
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
- Source path: [`TauLib/BookIII/Sectors/LanglandsReflection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Sectors/LanglandsReflection.lean#L50-L74)
- Source range: L50-L74
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D15` — Langlands₁ Reflection Bridge

## Immediate Comment / Docstring

```lean
/-- [III.D15] Langlands₁ reflection: maps E₀-sector data to E₁-sector data.
    The enrichment functor preserves the sector assignment when lifting
    from E₀ to E₁: for each boundary character χ, the E₁-enriched version
    of Φ(χ) has reduce-stable values at the E₁ level. -/
```

## Source Excerpt

```lean
def langlands_reflection_check (bound db : TauIdx) : Bool :=
  go 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (m n k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if m > bound then true
    else if n > bound then go (m + 1) 0 1 (fuel - 1)
    else if k > db then go m (n + 1) 1 (fuel - 1)
    else
      let χ : BoundaryCharacter := ⟨Int.ofNat m, Int.ofNat n⟩
      -- E₀ value
      let e0_val := boundary_to_interior χ 1 k
      -- E₁ enrichment: apply hom_stage
      let e1_val := hom_stage e0_val 0 k
      -- E₁ value should be reduce-stable (in the tower)
      let e1_stable := reduce e1_val k == e1_val
      -- E₀ → E₁ should preserve reduce-compatibility
      let flow_ok := reduce e0_val k == e0_val
      -- Tower coherence: E₁ value at k-1 agrees with projection
      -- (exercises Nat.mod_mod_of_dvd)
      let tower_ok := if k > 1 then
        reduce e1_val (k - 1) == reduce (reduce e1_val k) (k - 1)
      else true
      e1_stable && flow_ok && tower_ok && go m n (k + 1) (fuel - 1)
  termination_by fuel
```
