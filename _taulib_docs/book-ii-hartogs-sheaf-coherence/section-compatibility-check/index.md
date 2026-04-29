---
{
  "projection_kind": "taulib_declaration",
  "title": "section_compatibility_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/section-compatibility-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.SheafCoherence`.",
  "declaration_id": "TauLib.BookII.Hartogs.SheafCoherence::section_compatibility_check",
  "declaration_slug": "section-compatibility-check",
  "kind": "def",
  "name": "section_compatibility_check",
  "module_name": "TauLib.BookII.Hartogs.SheafCoherence",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/",
  "source_line_start": 342,
  "source_line_end": 363,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L342-L363",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.SheafCoherence",
        "url": "/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L342-L363",
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

- Module: [TauLib.BookII.Hartogs.SheafCoherence](/verify/taulib/docs/book-ii-hartogs-sheaf-coherence/)
- Source path: [`TauLib/BookII/Hartogs/SheafCoherence.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/SheafCoherence.lean#L342-L363)
- Source range: L342-L363
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Sections are reduce-compatible: if f is a section on C_{l,a} and
    we restrict to C_{k, reduce(a,k)}, the restriction equals
    reduce(f(x), k) for all x in C_{l,a}.

    In the primorial tower, "section" = "reduce-compatible value assignment,"
    so this is automatic. We verify the key case: the canonical section
    f(x) = x on [0, P_l) restricts to reduce(x, k) on the coarser cylinder. -/
```

## Source Excerpt

```lean
def section_compatibility_check (k_max : TauIdx) : Bool :=
  go_k 1 (k_max * 300 + 1)
where
  go_k (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k >= k_max then true
    else
      let pk1 := primorial (k + 1)
      let ok := check_compat 0 pk1 k
      ok && go_k (k + 1) (fuel - 1)
  termination_by fuel
  check_compat (x fuel k : Nat) : Bool :=
    if fuel = 0 then true
    else if x >= primorial (k + 1) then true
    else
      -- reduce(reduce(x, k+1), k) = reduce(x, k)
      let fine := reduce x (k + 1)
      let coarse_via_fine := reduce fine k
      let coarse_direct := reduce x k
      (coarse_via_fine == coarse_direct) &&
      check_compat (x + 1) (fuel - 1) k
  termination_by fuel
```
